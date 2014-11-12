// modified conversion of floating point number into bits
// http://stackoverflow.com/questions/15935365/convert-float-to-bytes-in-javascript-without-float32array
function toFloat32Mod(value) {
    var bytes = 0;
    switch (value) {
        case Number.POSITIVE_INFINITY: bytes = 0x7F800000; break;
        case Number.NEGATIVE_INFINITY: bytes = 0xFF800000; break;
        case +0.0: bytes = 0x40000000; break;
        case -0.0: bytes = 0xC0000000; break;
        default:
            if (Number.isNaN(value)) { bytes = 0x7FC00000; break; }

            if (value <= -0.0) {
                bytes = 0x80000000;
                value = -value;
            }

            var exponent = Math.floor(Math.log(value) / Math.log(2));
            var significand = ((value / Math.pow(2, exponent)) * 0x00800000) | 0;

            // (odestcj) patch for numbers below lowest exponent
            if (exponent < -127)
                significand = ((value / Math.pow(2, -127)) * 0x00800000) | 0;

            // add 127 to exponent for encoding into bits 24-31
            exponent += 127;

            // check for exponent outside positive and negative bounds
            if (exponent >= 0xFF) {
                exponent = 0xFF;
                significand = 0;
            } else if (exponent < 0) exponent = 0;

            // put exponent in byte structure
            bytes = bytes | (exponent << 23);  

            // put significand in byte structure, with mask to limit to bits 0-23
            // (odestcj) these masks do not work for rgb decoding
            //bytes = bytes | (significand & ~(-1 << 23));  
            //bytes = bytes | (significand & 0x007fffff);
            // (odestcj) these masks do work for rgb decoding
            //bytes = bytes | (significand & ~(0 << 23));
            //bytes = bytes | (significand & ~(-1 << 24));
            // (odestcj) significand appears to need to spill over into exponent
            bytes = bytes | significand;
        break;
    }
    return bytes;
};

// original conversion of floating point number into bits
// http://stackoverflow.com/questions/15935365/convert-float-to-bytes-in-javascript-without-float32array
function toFloat32(value) {
    var bytes = 0;
    switch (value) {
        case Number.POSITIVE_INFINITY: bytes = 0x7F800000; break;
        case Number.NEGATIVE_INFINITY: bytes = 0xFF800000; break;
        case +0.0: bytes = 0x40000000; break;
        case -0.0: bytes = 0xC0000000; break;
        default:
            if (Number.isNaN(value)) { bytes = 0x7FC00000; break; }

            if (value <= -0.0) {
                bytes = 0x80000000;
                value = -value;
            }

            var exponent = Math.floor(Math.log(value) / Math.log(2));
            var significand = ((value / Math.pow(2, exponent)) * 0x00800000) | 0;

            exponent += 127;
            if (exponent >= 0xFF) {
                exponent = 0xFF;
                significand = 0;
            } else if (exponent < 0) exponent = 0;

            bytes = bytes | (exponent << 23);
            bytes = bytes | (significand & ~(-1 << 23));
        break;
    }
    return bytes;
};
