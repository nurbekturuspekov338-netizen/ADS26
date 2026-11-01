import sys

class Max_heap:
    def __init__(self):
        self.heap=[]
        
    def _sift_up(self, idx):
        while idx>0:
            parent=(idx-1)//2
            if self.heap[idx]>self.heap[parent]:
                self.heap[idx], self.heap[parent]=(
                    self.heap[parent],
                    self.heap[idx]
                )
                idx=parent
            else:
                break
            
    def _sift_down(self, idx):
        n=len(self.heap)
        while True:
            largest=idx
            left=2*idx+1
            right=2*idx+2
            
            if left<n and self.heap[left]>self.heap[largest]:
                largest=left
            if right<n and self.heap[right]>self.heap[largest]:
                largest=right
            if largest!=idx:
                self.heap[idx], self.heap[largest]=(
                    self.heap[largest], 
                    self.heap[idx], 
                )       
                idx=largest
            else:
                break
    def add(self, x):
        self.heap.append(x)
        self._sift_up(len(self.heap)-1)
        
    def extract(self):
        max_val=self.heap[0]
        last=self.heap.pop()
        if self.heap:
            self.heap[0]=last
            self._sift_down(0)
        return max_val
    
def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return 
    
    n = int(lines[0])
    heap = Max_heap()
    
    for i in range(1, n + 1):
        if i >= len(lines):
            break
            
        parts = lines[i].split()
        if not parts:
            continue 
            
        op = parts[0]
        
        if op == "add":
            x = int(parts[1])
            heap.add(x)
        elif op == "extract":
            print(heap.extract())

if __name__ == "__main__":
    main()