# -*- coding: UTF-8 -*-
# Author: Junbin Zhang
# E-mail: p78083025@ncku.edu.tw
# Update time: 2021.03.21

from __future__ import print_function
import time

class CS():
    def __init__(self):
        self.cs = []
        self.cs_entry = []

        # Each router creates an independent cache space

    def Creat_cs(self, route_ID):
        '''
        cs = [[content_name, data, time, cost],
              ...
             ]
        '''
        return self.cs

        # Get cs

    def Get_cs(self, route_ID):
        return self.cs

        # Check if there is data matching the content name in cs

    def Search_cs_interest(self, cs, content_name):
        '''
        cs = [[content_name, data, time, cost],...]
        cs_entry = [content_name, data, time, cost]
        '''
        # self.cs = cs
        for cs_entry in cs:
            if content_name == cs_entry[0]:
                cs_entry[-2] += 1
                cs_entry[-1] = int(time.process_time()*1000)
                return True
        # No data for content name found in cs
        return False

        # Add an entry to CS

    def Creat_cs_entry(self, data, cs):
        '''
        cs = [[content_name, data, time, cost],...]
        cs_entry = [content_name, data, time, cost]
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0.0, 'path': ''}
        '''
        content_name = data['content_name']
        content_data = data['content_data']
        # Record the time this entry was created
        times = int(time.process_time()*1000 - data['run_start_time'])
        cost = data['data_hop']
        fre = 0     ##LFU
        recent_time = times     ##LRU
        cs_entry = [content_name, content_data, times, cost, fre, recent_time]
        cs.append(cs_entry)
        # return cs_entry

        # Delete an entry from CS

    def Remove_cs_entry(self, cs):
        '''
        cs = [[content_name, data, time, cost],...]
        '''
        cs.sort(key=lambda x:(x[-2]), reverse=False)
        # 1  5  10  15  20  30  40  50
        '''
        update_cache = 10
        if len(cs) != 0:
            temp = int(len(cs) * (update_cache / 100))
            for i in range(int((len(cs)-temp)/2), int((len(cs)+temp)/2)):
                index = i
                # Delete the most costly entry
                del cs[index]
        '''
        # 1  5  10  15  20  30  40  50
        
        update_cache = 10
        if len(cs) != 0:
            temp = int(len(cs) * (update_cache / 100))
            for i in range(0, temp):
                index = i
                # Delete the most costly entry
                del cs[index]
        
        # Cache data

    def Cache_cs_data(self, cs, cache_size, data):
        '''
        cs = [[content_name, data, time, cost],...]
        data = {'type': 'data', 'consumer_ID': 0, 'route_ID': 0, 'content_name': 'r0/0', 'content_data': '',
                'data_hop': 0, 'run_start_time': 0.0, 'path': ''}
        '''
        # self.cs = cs
        content_name = data['content_name']
        for cs_entry in cs:
            if content_name == cs_entry[0]:
                return
        # Check if CS is full
        if len(cs) > cache_size:
            # Remove the most costly entry
            self.Remove_cs_entry(cs)
        self.Creat_cs_entry(data, cs)
        # cs_entry =
        # cs.append(cs_entry)



    '''
    # Each router creates an independent cache space
    def Creat_cs(self, route_ID):

    # Get cs
    def Get_cs(self, route_ID):

    # Check if there is data matching the content name in cs
    def Search_cs_interest(self, cs, content_name):

    # Add an entry to CS
    def Creat_cs_entry(self, data, cs):


    # Delete an entry from CS
    def Remove_cs_entry(self, cs):

    # Cache data
    def Cache_cs_data(self, cs, cache_size, data):
    '''