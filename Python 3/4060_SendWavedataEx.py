import struct
import visa

rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

vi.encoding = 'latin-1' #vi.write_raw called from the vi.write needs the encoding changed

print(vi.query("*idn?"))

wave = bytearray()

for i in range(16384):
    wave.append(i&0xff)
    wave.append((i&0x3f00)>>8)
    
vi.write_termination = '' #the next commands should not be terminated with newline chars
vi.write(wave.decode('latin-1'))
print(2)
vi.write_termination = '\n' #the next commands should be terminated with newline char
    
cmd = "C1:wvdt m56,wvnm,chompipe,type,5,length,32KB,freq,1000,ampl,2,ofst,0,phase,0,wavedata,"
vi.write(cmd)
print(3)
resp = vi.query("C1:wvdt? m56")#Note, the return value shows mXX+6, so m36 => M42

print("returned....")
print(len(resp))

for i in range(32):
    print(resp[i])
