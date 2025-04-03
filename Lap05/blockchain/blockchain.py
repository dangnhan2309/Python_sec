import time
import hashlib
from block import Block

class Blockchain:
    def __init__(self):
        """Khởi tạo blockchain với block gốc (genesis block)"""
        self.chain = []
        self.current_transactions = []  # Danh sách giao dịch đang chờ xác nhận
        self.create_genesis_block()

    def create_genesis_block(self):
        """Tạo khối đầu tiên trong blockchain"""
        genesis_block = Block(0, "0", time.time(), [], 1)
        self.chain.append(genesis_block)

    def get_previous_block(self):
        """Lấy block cuối cùng của blockchain"""
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        """Thêm giao dịch vào danh sách giao dịch hiện tại"""
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })

    def proof_of_work(self, previous_proof):
        """Giải bài toán PoW để tìm proof hợp lệ"""
        new_proof = 1
        while not self.is_valid_proof(new_proof, previous_proof):
            new_proof += 1
        return new_proof

    def is_valid_proof(self, new_proof, previous_proof):
        """Kiểm tra proof có hợp lệ không"""
        guess = f"{new_proof}{previous_proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Điều kiện đơn giản: hash bắt đầu bằng "0000"

    def create_block(self, proof, previous_hash):
        """Tạo block mới và thêm vào blockchain"""
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_hash,
            timestamp=time.time(),
            transactions=self.current_transactions,
            proof=proof
        )
        self.chain.append(new_block)
        self.current_transactions = []  # Reset danh sách giao dịch
        return new_block

    def is_chain_valid(self, chain):
        """Kiểm tra blockchain có hợp lệ không"""
        for i in range(1, len(chain)):
            prev_block = chain[i - 1]
            current_block = chain[i]

            if current_block.previous_hash != prev_block.hash:
                return False

            if not self.is_valid_proof(current_block.proof, prev_block.proof):
                return False

        return True
