import hashlib
import requests

import sys

from uuid import uuid4
import time

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    - Note:  We are adding the hash of the last proof to a number/nonce for the new proof
    """

    start = time.time()

    print("Searching for next proof")
    proof = 0


    #  TODO: Your code herecd

    print("Searching for next proof")
    print('last proof: ', last_proof)
    # proof = int(time.time())
    proof = 0
    while valid_proof(last_proof, proof) is False:
        time_now = time.time()
        if time_now - start > 5:
            return
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    
    return proof


    # print('last proof: ', last_proof)
    # proof = int(time.time())
    # while valid_proof(last_proof, str(proof)) is False:
    #     time_now = time.time()
    #     if time_now - start > 10:
    #         print('restarting...')
    #         return
    #     proof *= 897

    # print("Proof found: " + str(proof) + " in " + str(timer() - start))
    # return proof

    # while valid_proof(last_proof, proof) is False:
    #     random_int = randint(1,7)
    #     proof+= random_int
    

    # print("Proof found: " + str(proof) + " in " + str(timer() - start))
    # return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the proof?

    IE:  last_hash: ...AE9123456, new hash 123456888...
    """

    # TODO: Your code here!
    guess = f'{proof}'.encode()
    hashed_p_prime = hashlib.sha256(guess).hexdigest()

    prev_proof = f'{last_hash}'.encode()
    hashed_p = hashlib.sha256(prev_proof).hexdigest()
    return hashed_p_prime[:6] == hashed_p[-6:]


    # guess = f'{last_hash}{proof}'.encode()ls
    # guess_hashed = hashlib.sha256(guess).hexdigest()

    # old_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()[-6:]
    # new_hash = hashlib.sha256(f'{proof}'.encode()).hexdigest()[:6]
    
    # return old_hash==new_hash

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()
    if len(id) == 0:
        f = open("my_id.txt", "w")
        # Generate a globally unique ID
        id = str(uuid4()).replace('-', '')
        print("Created new ID: " + id)
        f.write(id)
        f.close()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
            print("Total coins mined: " + str(coins_mined))
