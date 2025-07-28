# Use Python’s collections.deque to implement a browser history system with a maximum size of 5 pages. Your system should support:

# Add New Page – Append new page URLs to the end. If the size exceeds 5, remove the oldest page from the front.
# Go Back – Remove the last visited page (from end) and store it in a forward stack.
# Go Forward – Restore the most recently backed-out page from the forward stack to the end of the history.
# Maintain State – Track current history and forward stack after each action.
# Use two deque objects for history and forward_stack.

from collections import deque

class BrowserHistory:
    def __init__(self, max_size=5):
        self.history = deque(maxlen=max_size)
        self.forward_stack = deque()

    def add_page(self, url):
        self.history.append(url)
        self.forward_stack.clear()  
        print(f"Added page: {url}")
        print(f"Current history: {list(self.history)}")

    def go_back(self):
        if self.history:
            last_page = self.history.pop()
            self.forward_stack.append(last_page)
            print(f"Going back from: {last_page}")
        else:
            print("No pages to go back to.")
        print(f"Current history: {list(self.history)}")
        print(f"Forward stack: {list(self.forward_stack)}")

    def go_forward(self):
        if self.forward_stack:
            page_to_restore = self.forward_stack.pop()
            self.history.append(page_to_restore)
            print(f"Going forward to: {page_to_restore}")
        else:
            print("No pages to go forward to.")
        print(f"Current history: {list(self.history)}")
        print(f"Forward stack: {list(self.forward_stack)}")