# pylint: disable=E0202

import pybleno
import Error
import Success

class EndPosCharacteristic(pybleno.Characteristic):
    
    def __init__(self, move):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a2a1',
            'properties': ['read', 'write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a2a2',
                    'value': 'Gets or sets the End Position'
                })],
            'value': None
        })

        self.move = move
        
    def onReadRequest(self, offset, callback):
        if offset:
            Error.throw("Failed read in End Pos")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG, None)

        else:
            end_pos = (int) (self.move.end_pos * 100)
            data = end_pos.to_bytes(1, "big")
            Success.throw("Read End Pos")
            callback(pybleno.Characteristic.RESULT_SUCCESS, data)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("EndPos Data:")
        print(data)
        if offset:
            Error.throw("Failed write in End Pos (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in End Pos (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            print("parsed: " + str(parsed))
            val = parsed / 100
            if self.move.set_end_pos(val):
                Error.throw("Failed write in End Pos (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)

            else:
                Success.throw("Set End Pos: " + str(val))
                callback(pybleno.Characteristic.RESULT_SUCCESS)