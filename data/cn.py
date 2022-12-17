
# 600016 --> SH600016 // 300567 -->SZ300567
def codeToSymbol(code6):
    symbol = ''
    if len(code6) == 6:
        if code6[0] == '6' or code6[0] == '7' or code6[0] == '9':
            symbol = 'SH' + code6
        elif code6[0] == '3' or code6[0] == '0' or code6[0] == '2':
            symbol = 'SZ' + code6
        elif code6[0] == '4' or code6[0] == '8':
            symbol = 'BJ' + code6
        else:
            raise RuntimeError(f'Symbol Err: {code6}')
    return symbol

