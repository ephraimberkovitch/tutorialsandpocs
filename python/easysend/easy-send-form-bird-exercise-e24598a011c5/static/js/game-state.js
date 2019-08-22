var initialState = {
    width: 6,
    height: 7,
    moves: 0,
    tiles: [
        {x: 0, y: 0, type: tileTypes.nothing},
        {x: 1, y: 0, type: tileTypes.wall},
        {x: 2, y: 0, type: tileTypes.wall},
        {x: 3, y: 0, type: tileTypes.wall},
        {x: 4, y: 0, type: tileTypes.wall},
        {x: 5, y: 0, type: tileTypes.wall},

        {x: 0, y: 1, type: tileTypes.nothing},
        {x: 1, y: 1, type: tileTypes.wall},
        {x: 2, y: 1, type: tileTypes.floor},
        {x: 3, y: 1, type: tileTypes.floor},
        {x: 4, y: 1, type: tileTypes.floor},
        {x: 5, y: 1, type: tileTypes.wall},

        {x: 0, y: 2, type: tileTypes.wall},
        {x: 1, y: 2, type: tileTypes.wall},
        {x: 2, y: 2, type: tileTypes.wall},
        {x: 3, y: 2, type: tileTypes.floor},
        {x: 4, y: 2, type: tileTypes.floor},
        {x: 5, y: 2, type: tileTypes.wall},

        {x: 0, y: 3, type: tileTypes.wall},
        {x: 1, y: 3, type: tileTypes.floor},
        {x: 2, y: 3, type: tileTypes.floor},
        {x: 3, y: 3, type: tileTypes.floor},
        {x: 4, y: 3, type: tileTypes.floor},
        {x: 5, y: 3, type: tileTypes.wall},

        {x: 0, y: 4, type: tileTypes.wall},
        {x: 1, y: 4, type: tileTypes.floor},
        {x: 2, y: 4, type: tileTypes.floor},
        {x: 3, y: 4, type: tileTypes.floor},
        {x: 4, y: 4, type: tileTypes.wall},
        {x: 5, y: 4, type: tileTypes.wall},

        {x: 0, y: 5, type: tileTypes.wall},
        {x: 1, y: 5, type: tileTypes.floor},
        {x: 2, y: 5, type: tileTypes.floor},
        {x: 3, y: 5, type: tileTypes.floor},
        {x: 4, y: 5, type: tileTypes.wall},
        {x: 5, y: 5, type: tileTypes.nothing},

        {x: 0, y: 6, type: tileTypes.wall},
        {x: 1, y: 6, type: tileTypes.wall},
        {x: 2, y: 6, type: tileTypes.wall},
        {x: 3, y: 6, type: tileTypes.wall},
        {x: 4, y: 6, type: tileTypes.wall},
        {x: 5, y: 6, type: tileTypes.nothing},

        {x: 2, y: 1, type: tileTypes.finish},
        {x: 3, y: 1, type: tileTypes.finish},
        {x: 2, y: 4, type: tileTypes.form},
        {x: 2, y: 3, type: tileTypes.form},
        {x: 1, y: 5, type: tileTypes.player},
    ]
};
var gameState = JSON.parse(JSON.stringify(initialState));
function resetGameState() {
    gameState = JSON.parse(JSON.stringify(initialState));
}
var notMovingParts = Object();
function populateNotMovingPartsDict() {
    for (let tileState of gameState.tiles) {
        if (tileState.type == tileTypes.wall || tileState.type == tileTypes.finish)
            notMovingParts[""+tileState.x+"_"+tileState.y] = tileState.type;
    }
}

function freezeCurrentState() {
    return JSON.parse(JSON.stringify(gameState));
}

function undo() {
    if (currentIndex>0) {
        currentIndex--;
        redrawBoard();
    }
}

function redo() {
    if (currentIndex<hist.length-1) {
        currentIndex++;
        redrawBoard();
    }
}

var hist = new Array();
hist.push(freezeCurrentState());
var currentIndex = 0;

function updateHistory(newStep) {
    hist.push(newStep);
    currentIndex++;
}

function redrawBoard() {
    gameState = JSON.parse(JSON.stringify(hist[currentIndex]));
    initBoard();
}
