"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
    string encode(vector<string> strs) {
        ...Your code
        return encoded_string;
    }
    
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
        ...your code
        return strs;
    }
    
So Machine 1 does:
    string encoded_string = encode(strs);
and Machine 2 does:
    vector<string> strs2 = decode(encoded_string);
    
Approach 1: use extra character
Approach 2 (Optimal approach): adding 4 bits
"""
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_string = ""
        for s in strs:
            # store the length in 4 digits (zero-padded) + string itself
            encoded_string += str(len(s)).zfill(4) + s
        return encoded_string
    
    def encode(self, strs: List[str]) -> bytes:
        """Encodes a list of strings to bytes using 4-byte length prefix.
            This bytearray approach is the true "optimal" solution for production-level systems.
        """
        # This function uses real binary 4-byte header (range 0 to 2^32-1 per string).
        # Works with any Unicode character (utf-8 encoding).
        # Much closer to how serialization frameworks (gRPC, Protobuf, Thrift) handle it.
        # Efficient for network transfer (no extra delimiters).
        encoded = bytearray()
        for s in strs:
            data = s.encode("utf-8") # Converts string to bytes
            length = len(data).to_bytes(4, "big") # 4-byte length prefix
            encoded.extend(length)
            encoded.extend(data)
        return bytes(encoded)
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        response = []
        i = 0
        while i < len(s):
            # Read next 4 chars -> length
            length = int(s[i:i+4])
            i += 4
            # Extract that many characters
            response.append(s[i:i+length])
            i += length
        return response
    
    def decode(self, data: bytes) -> List[str]:
        """Decodes bytes back into list of strings."""
        response = []
        i = 0
        while i < len(data):
            length = int.from_bytes(data[i:i+4], "big") # read 4-byte length
            i += 4
            s = data[i:i+length].decode("utf-8") # read string
            response.append(s)
            i += length
        return response
    
codec = Codec()
input_data = ["hello", "my", "name", "is", "meet", ""]
encoded = codec.encode(input_data)
print("Encoded: ", encoded)

decoded = codec.decode(encoded)
print("Decoded String: ", decoded)