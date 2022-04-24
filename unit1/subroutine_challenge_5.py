def sound_file(sampl_freq, bit_depth, channels, dur):
    return sampl_freq * bit_depth * channels * dur


s = int(input("enter sampling frequency"))
b = int(input("enter bit depth"))
c = int(input("enter no. channels"))
d = int(input("enter duration"))
file_size = sound_file(s, b, c, d)

print(f"{file_size / (8 * 1024)}KB")
print(f"{file_size/ (8*1024*1024)}MB")