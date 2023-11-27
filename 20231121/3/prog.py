import sys
import struct

b = sys.stdin.buffer.read()
lenght = len(b)

tmp4_8 = struct.unpack("i", b[4:8])[0]
tmp20_22 = struct.unpack("h", b[20:22])[0]
tmp22_24 = struct.unpack("h", b[22:24])[0]
tmp24_28 = struct.unpack("i", b[24:28])[0]
tmp34_36 = struct.unpack("h", b[34:36])[0]
tmp40_44 = struct.unpack("i", b[40:44])[0]
a = [lenght < 44, b[:4] != b"RIFF", tmp4_8 != lenght - 8, b[8:12] != b"WAVE",  b[12:16] != b"fmt "]
a += [struct.unpack("i", b[16:20])[0] != 16, (tmp24_28 != 44100 and tmp24_28 != 48000), struct.unpack("i", b[28:32])[0] != (tmp24_28 * tmp34_36 * tmp22_24) / 8]
a += [struct.unpack("h", b[32:34])[0] != (tmp34_36 * tmp22_24) / 8, struct.unpack("h", b[32:34])[0] not in {1, 2, 4}, b[36:40] != b"data", tmp40_44 != tmp4_8 - 36]
if any(a):
    print("NO")
else:
    print(f"Size={tmp4_8}, Type={tmp20_22}, Channels={tmp22_24}, Rate={tmp24_28}, Bits={tmp34_36}, Data size={tmp40_44}")