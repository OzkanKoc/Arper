from scapy.all import srp,Ether,ARP
import sys

ans,unans=srp(Ether(dst='ff:ff:ff:ff:ff:ff')
              /ARP(pdst='192.168.1.0/24'),timeout=2,iface=availableIf,inter=0.2)

try:
        i_m=open("ipMac.txt","r")
        ipp=[]
        macc=[]
        for snd, rcv in ans:
                ipp.append(rcv.sprintf(r"%ARP.psrc%"))
                macc.append(rcv.sprintf(r"%ARP.hwsrc%"))
        
        a=i_m.readline()
        a=i_m.readline()
        f=0
        for k in range(0,(len(ipp))):
                i_m.seek(0)
                while len(a)!=0:
                        ip=""
                        mac=""
                        x=0
                        for i in range(len(a)):
                                if a[i]!=" " :
                                        if x==1:
                                                if len(mac)!=17:
                                                        mac+=a[i]
                                        else:
                                                ip+=a[i]
                                else:
                                        x=1
                        a=i_m.readline()
                        if ipp[k]==ip:
                                if macc[k]!=mac :
                                       print ipp[k]+' ip adresine ait mac adresi degismistir.'
                                else:
                                        f=1
                                break;
                        if macc[k]==mac:
                                if ipp[k]!=ip:
                                         print macc[k]+' mac adresine ait ip adresi degismistir.'
                                else:
                                        f=1
                                break;
                if f==0 :
                        s=raw_input(ipp[k]+' ip-mac adresi dosyada bulunmuyor. Eklemek ister misiniz? (y/n)')
                        if s=='y' or s=='Y':
                                i_m.close()
                                i_m=open("ipMac.txt","a")
                                i_m.write(ipp[k]+'                     '+
                                          macc[k]+'\n')
                                i_m.close()
                                i_m=open("ipMac.txt","r")
except:
        print "Dosya olusturuluyor.."
        i_m=open("ipMac.txt","w")
        i_m.write('---IP Address-------------------Mac Address---')
        for snd, rcv in ans:
                i_m.write('\n'+rcv.sprintf(r"%ARP.psrc%")+'                     '+
                  rcv.sprintf(r"%ARP.hwsrc%"))
finally:
        i_m.close()
