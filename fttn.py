onu = input('Serial da onu prks00 ')
caixa = str(input('Nro da caixa '))
caixazero = caixa.replace('0', '')
interfaceOLT = f'{caixa[3:4]}/{caixa[4:5]}'
ipgerencia = f'10.{caixazero[0:3]}.{caixazero[3:5]}.{caixazero[5:]}/24'
gw = f'10.{caixazero[0:3]}.{caixazero[3:5]}.65'
flow = f'{caixa[1:5]}'

print(f'''
remover onu
conf t
interface gpon{interfaceOLT}
no onu {caixa}

\033[31m=============================================\033[m

conf t
interface gpon {interfaceOLT}
onu prks00{onu} ip address {ipgerencia} gw {gw}

OLT-231# conf t
OLT-231(config)# interface gpon {interfaceOLT}                                                                                                                                                                                            
OLT-231(config-if)# onu prks00{onu} ip address {ipgerencia} gw {gw}                                                                                                                                                
OLT-231(config-if)# onu prks00{onu} flow-profile {flow}                                            
OLT-231(config-if)# onu prks00{onu} flow-profile 02_PROVISIONAMENTO                                                                                                                       
OLT-231(config-if)# onu prks00{onu} vlan-translation-profile _100 iphost
OLT-231(config-if)# onu prks00{onu} alias {caixa}                     
OLT-231(config-if)# exit

\033[31m=============================================
LOGAR NA ONU
=============================================\033[m

Username: admin
Password: parks
PARKS# configure terminal
PARKS(config)# aaa username admin level priviledged password v3tf77n
PARKS(config)# no ip routing
PARKS(config)# no ipv6 routing
PARKS(config)# no interface bridge0
PARKS(config)# no ip dhcp pool local
PARKS(config)# no ip domain lookup
PARKS(config)# no ip http server
PARKS(config)# hostname {caixa}
2322113(config)# bridge stp
2322113(config)# snmp-server community parks rw
2322113(config)# opmode bridge
%SYS-5: Configuration settings were reset to default bridge mode.
% Reload the system to effectuate the configuration changes.
2322113(config)# do copy r s
%SYS-6: Building Configuration.
2322113(config)# %SYS-5: Configuration saved.
exit

\033[31m=============================================
####### ONU CONFIGURADA EM MODO BRIDGE
=============================================\033[m
 
OLT-232# config terminal
OLT-232(config)# interface gpon{interfaceOLT}
OLT-232(config-if)# onu prks00{onu} flow-profile 3122
OLT-232(config-if)# onu prks00{onu} vlan-translation-profile _{flow} uni-port 1
OLT-232(config-if)# exit
''')