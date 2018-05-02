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
    wave.append(i&0xff00>>8)
    wave.append(i&0xff)
    
vi.write_termination = ''
cmd = wave.decode('latin-1') #Change to a string from the byte array
vi.write(cmd)

vi.write_termination = '\n' #the next commands should not be terminated with chars
    
cmd = "C1:wvdt m56,wvnm,paul,type,5,length,32KB,freq,1000,ampl,2,ofst,0,phase,0,wavedata,"
vi.write(cmd)

resp = vi.query("C1:wvdt m56?")#Note, the return value shows mXX+6, so m36 => M42

print("returned....")
print(len(resp))

for i in range(32):
    print(resp[i])
