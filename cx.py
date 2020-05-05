from socketIO_client import SocketIO, LoggingNamespace
import time

pl = ['{"VARh": [5629, 583754], "V Un L-N": [NaN, NaN, NaN, NaN], "IB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "kW": [15.5, 15.5, NaN, NaN], "VA H": [2.0198, 1.0672, 0.294, 0.5792, 0.1767, 0.1651, 0.2625], "F": [59.9349], "Wh": [434236, 6], "I Un": [NaN, NaN, NaN, NaN], "kVA": [69.5, 69.5, NaN, NaN], "IA H": [24.2298, 17.4999, 14.9814, 8.606, 10.104, 6.7647, 7.8315], "TDD": [2.201], "V L-L": [NaN, NaN, NaN, NaN], "THD I": [37.9809, NaN, NaN, NaN, NaN], "Demand": [0.0158, 0.0037], "kVAR": [-67.7, -67.7, NaN, NaN], "meter": "pm5320", "IC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "THD V L-L": [0.0, NaN, NaN, NaN], "VBC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "id": "exora-_-3", "V L-N": [229.1514, 229.1445, NaN, NaN], "DPF": ["0.2456 Leading", "0.2456 Leading", "nan Lagging", "nan Lagging"], "THD V L-N": [1.2068, 2.4135, NaN, NaN], "filter": "0", "V Un L-L": [NaN, NaN, NaN, NaN], "I": [0.3033, 0.3046, NaN, NaN], "PF": ["0.2234 Leading", "0.2234 Leading", "nan Lagging", "nan Lagging"], "VAh": [818648, 15], "VAB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VCA H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}',
'{"VARh": [5629, 583754], "V Un L-N": [NaN, NaN, NaN, NaN], "IB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "kW": [16.6, 16.6, NaN, NaN], "VA H": [2.0185, 1.0719, 0.294, 0.5792, 0.1767, 0.1651, 0.2626], "F": [59.9344], "Wh": [434236, 6], "I Un": [NaN, NaN, NaN, NaN], "kVA": [69.8, 69.8, NaN, NaN], "IA H": [25.283, 18.4274, 14.8805, 8.5481, 10.0359, 6.7191, 7.7788], "TDD": [2.2751], "V L-L": [NaN, NaN, NaN, NaN], "THD I": [38.9961, NaN, NaN, NaN, NaN], "Demand": [0.0158, 0.0037], "kVAR": [-67.8, -67.8, NaN, NaN], "meter": "pm5320", "IC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "THD V L-L": [0.0, NaN, NaN, NaN], "VBC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "id": "exora-_-3", "V L-N": [229.1445, 229.1445, NaN, NaN], "DPF": ["0.2613 Leading", "0.2613 Leading", "nan Lagging", "nan Lagging"], "THD V L-N": [1.2073, 2.4145, NaN, NaN], "filter": "0", "V Un L-L": [NaN, NaN, NaN, NaN], "I": [0.3046, 0.3046, NaN, NaN], "PF": ["0.2382 Leading", "0.2382 Leading", "nan Lagging", "nan Lagging"], "VAh": [818648, 15], "VAB H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VC H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "VCA H": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}']


def on_sent(args):
    print('Data Sent Successfully')

for x in range(0,2):
    socketIO = SocketIO('localhost', 8000, LoggingNamespace)
    socketIO.on('sent', on_sent)
    socketIO.emit('my_broadcast_event', {'data': str(pl[x])})
    socketIO.wait(seconds=1)