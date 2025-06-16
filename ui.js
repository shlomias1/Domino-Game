const game = new DominoGame(2);

const boardDiv = document.getElementById("board");
const handDiv = document.getElementById("hand");
const infoDiv = document.getElementById("info");
const drawBtn = document.getElementById("draw-btn");

function updateUI() {
  // Update board
  boardDiv.innerHTML = "";
  const tiles = game.currentBoard();
  tiles.forEach(tile => {
    const el = document.createElement("div");
    el.className = "tile";
    el.textContent = `[${tile[0]}|${tile[1]}]`;
    boardDiv.appendChild(el);
  });

  // Update hand
  handDiv.innerHTML = "";
  const hand = game.playerHand(game.currentPlayer);
  hand.forEach(tile => {
    const btn = document.createElement("button");
    btn.textContent = `[${tile[0]}|${tile[1]}]`;
    btn.className = "tile";
    if (game.validMoves(tile)) {
      btn.classList.add("green");
      btn.onclick = () => {
        if (game.playTile(game.currentPlayer, tile)) {
          const winner = game.hasWinner();
          if (winner >= 0) {
            alert(`Player ${winner + 1} wins!`);
            location.reload();
          } else {
            game.nextTurn();
            updateUI();
          }
        }
      };
    } else {
      btn.classList.add("red");
      btn.disabled = true;
    }
    handDiv.appendChild(btn);
  });

  // Update info
  infoDiv.textContent = `Player ${game.currentPlayer + 1}'s Turn`;
}

drawBtn.onclick = () => {
  const tile = game.drawTile(game.currentPlayer);
  if (tile) {
    alert(`You drew: [${tile[0]}|${tile[1]}]`);
  } else {
    alert("No tiles left in stock.");
  }
  updateUI();
};

updateUI();