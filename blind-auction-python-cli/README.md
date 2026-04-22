# 🕶️ Blind Auction Python CLI Tool  

A simple and beginner-friendly **Blind Auction system** built using Python. This CLI-based project allows multiple users to place bids anonymously and determines the highest bidder.

---

## 🚀 Features  

- Supports multiple bidders  
- Accepts bid amounts securely (blind bidding)  
- Automatically determines the highest bidder  
- Clears terminal screen between bidders for privacy  
- Handles invalid inputs gracefully  
- Interactive command-line interface  

---

## 🧠 How It Works  

The Blind Auction system collects bids from multiple users without revealing previous bids. Each participant enters their name and bid amount, and once all bids are placed, the system calculates the highest bidder.

**Example flow:**  

- User 1 → enters name & bid  
- Screen clears  
- User 2 → enters name & bid  
- ...  
- Winner is announced at the end  

---

## 🛠️ Tech Stack  

- Python 3  
- CLI (Command Line Interface)  

---

## 💻 Usage  

What is your name?
Alice

Enter your bid amount: $100

Are there other bidders? (yes/no): yes

What is your name?
Bob

Enter your bid amount: $150

Are there other bidders? (yes/no): no


**Output:**  🏆 Winner: Bob with a bid of $150


---

## ⚠️ Input Rules  

- Bid amount must be a number  
- Invalid inputs will prompt retry  
- Only `yes` or `no` should be entered for continuation  

---

## 🧩 Future Improvements  

- Completely hide bidder names (true blind mode)  
- Store results in a file or database  
- Convert into a web app using Flask  
- Improve UI using advanced CLI libraries like `rich`  

---

## 🤝 Contributing  

Pull requests are welcome! Feel free to fork this repo and improve it.  

---

## ⭐ Support  

If you like this project, give it a star ⭐ on GitHub!  
