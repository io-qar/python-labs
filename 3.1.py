import struct

DSIZE = 1 + 1 + 4 + 4 + 2 + 1 + 4 + 4
CSIZE = 4 + 8
BSIZE = 4 + 1 + 4 + 4 + 4 + 4 + 4 + 2 + 2 + 4
ASIZE = 2 + 4 + 8 + 2 + 2 + 2 + 4 + 4 + 2

def parseD(offset, byteString):
	dBytes = byteString[offset: offset + DSIZE]
	dParsed = struct.unpack('<BBIIHbiI', dBytes)

	d4Bytes = byteString[dParsed[4]:dParsed[4] + dParsed[3] * 8]
	d4Parsed = struct.unpack('<' + 'q' * dParsed[3], d4Bytes)

	return {
		'D1': dParsed[0],
		'D2': dParsed[1],
		'D3': dParsed[2],
		'D4': list(d4Parsed),
		'D5': dParsed[5],
		'D6': dParsed[6],
		'D7': dParsed[7]
	}

def parseC(offset, byteString):
	cBytes = byteString[offset: offset + CSIZE]
	cParsed = struct.unpack('<IQ', cBytes)

	return {
		'C1': cParsed[0],
		'C2': cParsed[1]
	}

def parseB(offset, byteString):
	bBytes = byteString[offset: offset + BSIZE]
	bParsed = struct.unpack('<ibifiIIHHi', bBytes)
	
	b6Bytes = byteString[bParsed[6]:bParsed[6] + bParsed[5] * 4]
	b6Parsed = struct.unpack('<' + 'I' * bParsed[5], b6Bytes)
	b6List = [parseC(addr, byteString) for addr in b6Parsed]

	dStructCount = bParsed[7]
	dStructAddr = bParsed[8]
	b7List = []

	for i in range(dStructCount):
		b7List.append(parseD(dStructAddr + DSIZE * i, byteString))

	return {
		'B1': bParsed[0],
		'B2': bParsed[1],
		'B3': bParsed[2],
		'B4': bParsed[3],
		'B5': bParsed[4],
		'B6': b6List,
		'B7': b7List,
		'B8': bParsed[9]
	}

def parseA(offset, byteString):
	aBytes = byteString[offset:offset + ASIZE]
	aParsed = struct.unpack('<' + 'HIdHHHIIh', aBytes)

	a5Bytes = byteString[aParsed[5]:aParsed[5] + aParsed[4] * 4]
	a5Parsed = struct.unpack('<' + 'I' * aParsed[4], a5Bytes)

	a6Bytes = byteString[aParsed[7]:aParsed[7] + aParsed[6] * 2]
	a6Parsed = struct.unpack('<' + 'h' * aParsed[6], a6Bytes)

	return {
		'A1': parseB(aParsed[0], byteString),
		'A2': aParsed[1],
		'A3': aParsed[2],
		'A4': aParsed[3],
		'A5': list(a5Parsed),
		'A6': list(a6Parsed),
		'A7': aParsed[8]
	}

def f31(byteString):
	return parseA(5, byteString)

print(f31(
		b'QRZSB\x8d\x00>\xf2(\xbf\x18\xa49\xb9\x87{\xe2?\n\x95\x02\x00\xae'
		b'\x00\x03\x00\x00\x00\xb6\x00\x00\x00\xbc\xe3\xcfQB\xdb\xf5\x1c-s\xd4'
		b'\x05\x07w\x98\xd6\xee\xe5j\xf0\xe0\xbc#(\x06.#\x00\x00\x00/\x00\x00\x00\xc1'
		b'\xef\xeb9\xb5\x1f|D\xebD\xb2\xba8\x12<\x19v\xf6\xe5h)\x94N\x1a\xd3'
		b'\xf3\x8d\x199r#u\xcf\xd3G\xf4\xc5c\x02\x00\x00\x00C\x00Xb\xec\xadP\xc1F\x15@'
		b'" \xa2)\xa5\xf2\x02\x00\x00\x00S\x00\x02}8^\xeb\xcd\x19\xf1\x05\x0b\tE'
		b'\xc1\x84\x83\x16\xf9\xf3\x88\x9b\x18\xbf\x12)\x93\xc7\x02\x00\x00\x00;\x00'
		b'\x00\x00\x02\x00c\x00j>c\xc6\x02%dy\xc4\xe8$\x1b\xbesO\x11\xe9H'
	)
)