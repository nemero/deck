#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from time import sleep
import random
import threading
from threading import Thread

clients = {}
listeners = {}
terminate = False
engine = None


class Player(object):
    """Class Player. Constructor takes the Player Name"""
    def __init__(self, name, *args):
        super(Player, self).__init__()
        self.name = name
        self.cards = []
        self.aces, self.total = 0, 0


    def add_card(self, card):
        self.aces += 1 if card == 11 else 0
        self.total += card
        self.cards.append(card)

        return True


    def get_subtotal(self):
        totals = [self.total]
        for ace in range(1, self.aces + 1):
            totals.append(self.total - 10*ace)

        return totals

    def clear(self):
        self.aces = 0
        self.total = 0
        self.cards = []


class Table:
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.raw = []

    def header(self):
        self.raw.append('Name            | Points ')
        self.raw.append('----------------|---------')

    def row(self, player):
        self.raw.append(player['name'] + '   | ' + str(player['points']))

    def footer(self):
        self.raw.append('--------------------------')       


class Engine:
    """docstring for Engine"""
    deck = []
    players = {}
    results = []

    def __init__(self):
        super(Engine, self).__init__()
        print('Welcome to SuperDeck Game 21!')
        self.setting()

    def setting(self):
        # Generate Deck
        cards = [2, 3, 4, 6, 7, 8, 9, 10, 11]
        [self.deck.extend(cards) for c in range(0, 4)]

    def add_player(self, player):
        #if int(self.count_players) < len(self.players):
        self.players[player.name] = {'player': player, 'completed': False}

    def get_card(self, player):
        drop = random.choice(self.deck)
        self.deck.remove(drop)
        player.add_card(drop)
        totals = player.get_subtotal()
        return str(drop) + ' subtotals:' + '/'.join([str(x) for x in totals]) 

    def finish(self, player):
        print(self.players, player.name)
        self.players[player.name]['completed'] = True

        # if all players take cards will calculate winner
        show_reslt = True
        for idx in self.players:
            if not self.players[idx]['completed']:
                show_reslt = False
                break

        if show_reslt:
            for idx in self.players:
                player = self.players[idx]['player']
                totals = player.get_subtotal()

                final = False
                for temp in totals:
                    if (final == False or (final < temp <= 21) or (temp < final > 21)):
                        final = temp

                self.results.append({'name': player.name, 'points': final, 'cards': len(player.cards)})

            return self.run()

    def run(self):
        table = Table()
        table.header()
        for player in self.results:
            table.row(player)
        table.footer()

        # Depend winner
        winner = {'name': '', 'points': False, 'cards': 0}

        # sorting
        for player in self.results:
            if (winner['points'] == False
                or (winner['points'] < player['points'] <= 21)
                or (player['points'] < winner['points'] > 21)
                or (player['points'] == winner['points'] and player['cards'] < winner['cards'])
               ):
                winner = player

        self.results = []
        self.setting()
        for idx in self.players:
            self.players[idx]['player'].clear()
            self.players[idx]['completed'] = False

        msg = '\n'.join(table.raw) + '\nCongratulations ' + winner['name'] + ' is win. With score ' + str(winner['points']) + ' points'
        return msg


class ClientThread(Thread):
    """docstring for ClientThread
        Commands for client:
        online
        take - for get card
        finish = for finish game and waiting other players
    """
    player = None
    
    def __init__(self, name, conn, addr):
        super(ClientThread, self).__init__()
        self.name = name
        self.conn = conn
        self.addr = addr

    def base_str(self):
        ip, port = self.addr
        return '[Client]: ' + str(ip) + ' ' + str(port)

    def run(self):
        """Launch thread"""
        ip, port = self.addr
        print(self.base_str(), 'is started.')
        for idx in clients:
            if clients[idx]['address'] == self.addr:
                self.player = Player(self.name)
                clients[idx]['player'] = self.player
                engine.add_player(self.player)

        
        while not terminate:
            data = self.conn.recv(1024)

            if data.decode() in dir(self):
                func = getattr(self, data.decode())
                func()
            elif data:
                print(self.base_str(), 'message:', data.decode())
                msg = self.base_str() + ' message: ' + data.decode()
                for idx in clients:
                    if (port not in clients[idx]['address']):
                        clients[idx]['connect'].send(msg.encode())
            else: 
                break

            sleep(1)

    def online(self):
        data = 'Current online: ' + str(len(clients))
        self.conn.send(data.encode())

    def take(self):
        card = engine.get_card(self.player)
        self.conn.send(card.encode())   

    def finish(self):
        data = engine.finish(self.player)  
        if data:
            print(data)
            for idx in clients:
                clients[idx]['connect'].send(data.encode())



class MonitorThread(Thread):
    """docstring for MonitorThread"""
    def __init__(self, name):
        super(MonitorThread, self).__init__()
        self.name = name

    def run(self):
        """Launch thread"""
        while not terminate:
            index_del = []
            for idx in clients:
                #print(client.is_alive(), client.ident)
                if clients[idx]['thread'].is_alive() == False and clients[idx]['thread'].ident != None:
                    ip, port = clients[idx]['address']
                    print('[Client]:', ip, port, clients[idx]['thread'].name, 'is terminated.')
                    index_del.append(idx)

            # Remove terminated threads from client list
            if len(index_del):
                # need lock theards until we clear peers
                for idx in index_del:
                    del clients[idx]

            sleep(5)

        print('[Server]: Monitor is stopped.')


class Listener(object):
    """docstring for Listener"""
    sock = None

    def __init__(self):
        super(Listener, self).__init__()
        self.sock = socket.socket()
        self.sock.bind(('', 8080))
        self.sock.listen(1)

    def run(self):
        conn, addr = self.sock.accept()
        client_number = len(clients) + 1
        clients[client_number] = {
            'thread': ClientThread('client-' + str(client_number), conn, addr),
            'connect': conn,
            'address': addr
        }
        clients[client_number]['thread'].setDaemon(True)
        clients[client_number]['thread'].start()

        self.run()
        

if __name__ == "__main__":
    monitor = MonitorThread('monitor-1')
    #monitor.setDaemon(True)
    monitor.start()

    engine = Engine()

    try:
        listener = Listener()
        listener.run()
    except Exception as e:
        print(e.strerror)
        listener.sock.close()
        terminate = True

    # listener = Listener()
    # listener.run()

    #listener.sock.close()
    # clients[0] = ClientThread('client-1')
    # clients[1] = ClientThread('client-2')

    # clients[0].setDaemon(True)
    # clients[0].start()

    # clients[1].setDaemon(True)
    # clients[1].start()
    
        