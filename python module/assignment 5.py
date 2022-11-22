sentence = 'good for all'
sent_list = list(sentence)
sent_list[0] = 'f'
sent_list[-1] = '?'
'.'.join(sent_list)