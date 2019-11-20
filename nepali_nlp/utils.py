def load_multiple_link_dataset(file_loc = 'nep-eng.txt'):
    with open(file_loc,'r') as fp:
        file_content = []
        file_ = fp.read().splitlines()

        for ind,item in enumerate(file_):
            if item:
                if not item.isspace():
                    file_content.append(item)

    file_content[0] = 'aba'
    unicode_ = []; preeti=[]; pos=[]; meaning=[]
    c = 0
    for ind, item in enumerate(file_content):
        if c==0:
            unicode_.append(item)
            c = c + 1
        elif c==1:
            preeti.append(item)
            c = c + 1
        elif c==2:
            pos.append(item)
            c = c + 1
        else:
            meaning.append(item)
            c = 0
    
    return unicode_,preeti,pos,meaning