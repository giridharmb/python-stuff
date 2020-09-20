import hashlib
import multiprocessing
import time

data = ('851e39a3-5fc1-46f8-8456-f2855c71968c', 'd7c9ac0f-4874-4e8d-8ece-64a5299e7873', 'ee51142c-cefd-4e84-ab6d-d152ee0aec43', '88a97c3c-f564-4aca-a330-22a0b8b5765c', '730bad29-4d8c-4823-a2f4-01ee7c9731cd', 'f7237383-03b3-44b9-803c-a0ee4658f832', 'f366042c-1015-4afa-861e-e8052fdcdd82', 'e62f980d-9bb7-41c8-8905-e38ef810339d', '927d044c-0ee5-4282-8690-5e3f618b13e8', '494bb90c-11e4-48e1-8d95-9bfddc14749f', 'c8e0a833-4d8b-4e6e-982a-67cd41225d06', '2a04a980-6439-48cb-9d75-8026ad28342a', 'b379ab3f-13f1-4cc5-a827-8e9d56a35e12', '51c380dd-c21c-44d6-a1fa-edb3a6af339d', '338539d7-2723-4d23-a3cf-c1bab97698f5', '2c4ab78f-7220-4da8-9e48-5d32c2959f27', '90b91b40-0d28-4fbd-a15e-defd652983f2', '6fccc4d7-b27f-4e7a-a800-fccefcbc1580', 'd6c77210-9be9-44fb-a4c0-62b457641169', 'f591ba9b-3c7b-4945-b6d1-caa295191aac')

def getMD5Hash(myString):
    time.sleep(3)
    return str(hashlib.md5(myString.encode("utf-8")).hexdigest())

def mp_worker((inputs)):
    print(" Processs %s" % (inputs))
    getMD5Hash(inputs)
    time.sleep(int(3))
    print(" Process %s \t DONE" % inputs)

def mp_handler():
    p = multiprocessing.Pool(3)
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()