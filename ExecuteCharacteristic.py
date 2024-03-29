# pylint: disable=E0202

import pybleno
import Error
import Success

class ExecuteCharacteristic(pybleno.Characteristic):
    
    def __init__(self, move):
        pybleno.Characteristic.__init__(self, {
            'uuid': 'a4a1',
            'properties': ['write'],
            'descriptors': [
                pybleno.Descriptor({
                    'uuid': 'a4a2',
                    'value': 'Starts the Move'
                })],
            'value': None
        })

        self.move = move

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        print("Execute Data:")
        print(data)
        if offset:
            Error.throw("Failed write in Execute (#1)")
            callback(pybleno.Characteristic.RESULT_ATTR_NOT_LONG)

        elif len(data) != 1:
            Error.throw("Failed write in Execute (#2)")
            callback(pybleno.Characteristic.RESULT_INVALID_ATTRIBUTE_LENGTH)

        else:
            parsed = int.from_bytes(data, byteorder='big', signed=False)
            if parsed == 1:
                Success.throw("Started Exec")
                if self.move.execute_move():
                    Error.throw("Execution Failed")
                    callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)
                else:
                    Success.throw("Execution Completed")
                    callback(pybleno.Characteristic.RESULT_SUCCESS)
            elif parsed == 0:
                Success.throw("Wrote 0 to Execute")
                callback(pybleno.Characteristic.RESULT_SUCCESS)

            else:
                Error.throw("Failed write in Execute (#3)")
                callback(pybleno.Characteristic.RESULT_UNLIKELY_ERROR)
