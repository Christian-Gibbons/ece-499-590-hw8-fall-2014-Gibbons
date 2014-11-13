from ctypes import Structure,c_uint16,c_double,c_ubyte,c_uint32,c_int16

CV_REF_NAME = 'cv-ref-chan'

class CV_REF(Structure):
	_pack_ = 1
	_fields_ = [("setX",    c_int16),
                ("setY",    c_int16),
				("X",		c_int16),
				("Y",		c_int16)]
