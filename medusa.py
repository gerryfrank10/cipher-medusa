import optparse
from os import *

def main():
    print ("***************************************************************")
    print (r"   |\       /|  |-----  |--\   |    |   /----         /-\     ")
    print (r"   | \     / |  |_____  |   |  |    |   |            /   \    ")
    print (r"   |  \   /  |  |       |   |  |    |   ----\       /_____\    ")
    print (r"   |   \ /   |  |----   |--/    \__/    ____|      /       \  ")
    print ()
    print ("***************************************************************")
    print ()
    parser = optparse.OptionParser("usage of program is -e <text or file to encrypt> mode or -d <text or file to decrypt> mode ")
    parser.add_option('-e', dest='encrypt', type='string', help='Encrypt with different mode <caesar> <vinegre> <rsa>')
    parser.add_option('-k', dest='key', type='int', help='The key to encrypt')
    parser.add_option('-d', dest='decrypt', type='string', help='The key to decrypt')
    parser.add_option('-t', dest='txt', type='string', help='the message')
    parser.add_option('-K', dest='Key', type='string', help='The rsa key to encrypt or decrypt')
    #parser.add_option('-g',dest='generate', type='string', help='Generate your keys')
    (options, args) = parser.parse_args()
    enc = options.encrypt
    dec = options.decrypt
    key = options.key
    txt = options.txt
    Key = options.Key
    if enc == None and dec == None:
        print(parser.usage)
        exit(0)
    if enc == 'caesar':
        import caesar
        translate = caesar.Ecaesar(txt, key)
        print (translate)
        exit(0)
    elif enc == 'vinegre':
        msg = Evinegre(enc)
        print (msg)
        exit(0)
    elif enc == 'rsa':
        from rsa import Ersa
        msg = Ersa(txt, Key)
        print (msg)
        exit(0)
    if dec == 'caesar':
        from caesar import Dcaesar
        translate = Dcaesar(txt, key)
        exit(0)
    elif dec == 'rsa':
        from rsa import Drsa
        msg = Drsa(txt, Key)
        print (msg)
        exit(0)
if __name__ == '__main__':
    main()
