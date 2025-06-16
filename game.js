class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class LinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
    }
  
    isEmpty() {
      return this.head === null;
    }
  
    addToHead(value) {
      const node = new Node(value);
      if (this.isEmpty()) {
        this.head = this.tail = node;
      } else {
        node.next = this.head;
        this.head = node;
      }
    }
  
    addToTail(value) {
      const node = new Node(value);
      if (this.isEmpty()) {
        this.head = this.tail = node;
      } else {
        this.tail.next = node;
        this.tail = node;
      }
    }
  
    toArray() {
      const arr = [];
      let curr = this.head;
      while (curr) {
        arr.push(curr.value);
        curr = curr.next;
      }
      return arr;
    }
  }
  
  class DominoGame {
    constructor(numPlayers) {
      this.numPlayers = numPlayers;
      this.players = Array.from({ length: numPlayers }, () => []);
      this.board = new LinkedList();
      this.stock = this.generateTiles();
      this.currentPlayer = 0;
      this.distribute();
    }
  
    generateTiles() {
      const tiles = [];
      for (let i = 0; i <= 6; i++) {
        for (let j = i; j <= 6; j++) {
          tiles.push([i, j]);
        }
      }
      return tiles.sort(() => Math.random() - 0.5);
    }
  
    distribute() {
      const count = this.numPlayers === 2 ? 7 : 5;
      for (let i = 0; i < this.numPlayers; i++) {
        for (let j = 0; j < count; j++) {
          this.players[i].push(this.stock.pop());
        }
      }
    }
  
    currentBoard() {
      return this.board.toArray();
    }
  
    validMoves(tile) {
      if (!this.board.head) return true;
      const left = this.board.head.value[0];
      const right = this.board.tail.value[1];
      return [tile[0], tile[1]].includes(left) || [tile[0], tile[1]].includes(right);
    }
  
    playTile(playerIdx, tile) {
      if (!this.board.head) {
        this.board.addToHead(tile);
      } else {
        const left = this.board.head.value[0];
        const right = this.board.tail.value[1];
  
        if (tile[1] === left) {
          this.board.addToHead(tile);
        } else if (tile[0] === left) {
          this.board.addToHead([tile[1], tile[0]]);
        } else if (tile[0] === right) {
          this.board.addToTail(tile);
        } else if (tile[1] === right) {
          this.board.addToTail([tile[1], tile[0]]);
        } else {
          return false;
        }
      }
  
      const idx = this.players[playerIdx].findIndex(t => t[0] === tile[0] && t[1] === tile[1]);
      if (idx >= 0) this.players[playerIdx].splice(idx, 1);
      return true;
    }
  
    drawTile(playerIdx) {
      if (this.stock.length > 0) {
        const tile = this.stock.pop();
        this.players[playerIdx].push(tile);
        return tile;
      }
      return null;
    }
  
    hasWinner() {
      return this.players.findIndex(hand => hand.length === 0);
    }
  
    nextTurn() {
      this.currentPlayer = (this.currentPlayer + 1) % this.numPlayers;
    }
  
    playerHand(playerIdx) {
      return this.players[playerIdx];
    }
  }  