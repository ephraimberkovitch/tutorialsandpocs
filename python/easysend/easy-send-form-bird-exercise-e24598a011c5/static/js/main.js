var gameBoardElem;

var playerInfo = {
    state: undefined,
    elem: undefined,
};

var formInfos = [];

window.onload = function () {
    initBoard();
    populateNotMovingPartsDict();
    initEventListeners();
};

function initBoard() {
    resetBoardState();
}

function resetBoardState() {
    setBoardSize();
    createBoardTiles();
    updateUi();
}

function movePlayerInDirection({x, y}) {

    let newPos = {
        x: playerInfo.state.x + x,
        y: playerInfo.state.y + y,
    };

    if (isWallAt(newPos)) {
        return false;
    }

    let formInfo = getFormInfoAt(newPos);
    if (formInfo !== undefined) {
        let newFormPos = {
            x: formInfo.state.x + x,
            y: formInfo.state.y + y,
        };

        if (isWallOrFormAt(newFormPos)) {
            return false;
        }

        moveTile(formInfo, {x, y});
    }

    moveTile(playerInfo, {x, y})

    gameState.moves++;

    var newState = freezeCurrentState();
    updateHistory(newState);

    updateUi();
    checkGameWon();
    return true;
}

function onKeyDown(e) {
    let keyCode = e.keyCode;

    if (keyCode === KEY_LEFT ||
            keyCode === KEY_UP ||
            keyCode === KEY_RIGHT ||
            keyCode === KEY_DOWN) {
        let direction;

        switch(e.keyCode) {
            case KEY_LEFT:
                direction = {x: -1, y: 0}
                break;
            case KEY_RIGHT:
                direction = {x: 1, y: 0}
                break;
            case KEY_UP:
                direction = {x: 0, y: -1}
                break;
            case KEY_DOWN:
                direction = {x: 0, y: 1}
                break;
        }
        movePlayerInDirection(direction);
    }
}

function initEventListeners() {
    document.onkeydown = onKeyDown;
}

function setBoardSize() {
    gameBoardElem = document.getElementById('game-board');
    gameBoardElem.style.width = `${gameState.width * tileSize}px`;
    gameBoardElem.style.height = `${gameState.height * tileSize}px`;
}

function createBoardTiles() {
    playerInfo = undefined;
    formInfos = [];

    gameBoardElem.innerHTML = '';
    for (let tileState of gameState.tiles) {
        var tileElem = document.createElement('div');
        tileElem.style.width = `${tileSize}px`;
        tileElem.style.height = `${tileSize}px`;
        tileElem.style.left = `${tileState.x * tileSize}px`;
        tileElem.style.top = `${tileState.y * tileSize}px`;
        tileElem.className = `tile tile-${tileState.type}`;
        gameBoardElem.appendChild(tileElem);

        let tileInfo = {
            state: tileState,
            elem: tileElem
        }

        if (tileState.type === tileTypes.player) {
            playerInfo = tileInfo;
        }

        if (tileState.type === tileTypes.form) {
            formInfos.push(tileInfo);
        }
    }
}

function moveTile(tileInfo, {x, y}) {
    tileInfo.state.x += x;
    tileInfo.state.y += y;
}

function repositionTileUi(tileInfo) {
    tileInfo.elem.style.left = `${tileInfo.state.x * tileSize}px`;
    tileInfo.elem.style.top = `${tileInfo.state.y * tileSize}px`;
    // tileInfo.elem.style.animation = 'pulse 1s infinite';
}

function updateUi() {
    repositionTileUi(playerInfo);
    for (let formInfo of formInfos) {
        repositionTileUi(formInfo);
    }

    document.getElementById('game-info-moves').innerText = gameState.moves;
}

function isWallAt(pos) {
    return isTileTypeAt(pos, tileTypes.wall);
}

function isWallOrFormAt(pos) {
    return isWallAt(pos) || (getFormInfoAt(pos) !== undefined);
}

function isFinishAt(pos) {
    return isTileTypeAt(pos, tileTypes.finish);
}

function isTileTypeAt({x, y}, tileType) {
    return notMovingParts[""+x+"_"+y] == tileType;
    /*for (let tileState of gameState.tiles) {
        if (x === tileState.x && y === tileState.y && tileType === tileState.type) {
            return true;
        }
    }

    return false;*/
}

function getFormInfoAt({x, y}) {
    for (let formInfo of formInfos) {
        if (x === formInfo.state.x && y === formInfo.state.y) {
            return formInfo;
        }
    }

    return undefined;
}

function isGameWon() {
    for (let formInfo of formInfos) {
        if (!isFinishAt(formInfo.state)) {
            return false;
        }
    }
    return true;
}

function checkGameWon() {
    if (isGameWon()) {
        window.location.href = '/static/win.html';
    }
}

function newGame() {
    resetGameState();
    initBoard();
}
