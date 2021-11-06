


var piece = "";
var pieceIsSelected = 0;


function move(element) {
    if (pieceIsSelected == 1) {
        //put the piece down
        document.getElementById(element.id).innerHTML = piece;
        pieceIsSelected = 0;
    }//if
    else {
        if (element.textContent.trim() != '') {
            //square is not empty, pick up the piece
           piece = element.textContent;
           element.innerHTML = "";
           pieceIsSelected = 1;
        }
    }
}//move()