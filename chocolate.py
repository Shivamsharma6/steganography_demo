from steganography.steganography import Steganography

for a in range(1,11):
    op='secret'+str(a)+'.jpg'
    secret_text = Steganography.decode(op)
    print 'This is your secret message of %d image:' %(a)
    print secret_text
