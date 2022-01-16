import redlab as rl

print("------- einzelne Werte -------------------------")
print("16 Bit Value: " + str(rl.cbAIn(0,0,1)))
print("Voltage Value: " + str(rl.cbVIn(0,0,1)))
print("------- Messreihe -------------------------")
print("Messreihe: " + str(rl.cbAInScan(0,0,0,300,8000,1)))
print("Messreihe: " + str(rl.cbVInScan(0,0,0,300,8000,1)))
print("Samplerate: " + str(rl.cbInScanRate(0,0,0,8000)))
print("------- Ausgabe -------------------------")
print("Voltage Value: " + str(rl.cbVOut(0,0,101,2.5)))