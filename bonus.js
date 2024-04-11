// given m by n matrix
// contains -1 in certain cells
// 1. make a copy of matrix
// 2. replace -1 with max value of that column in the matrix
// 3. return the matrix

// Q: are all values in the matrix guarenteed to me numbers: Y


// Example 1:
// [1,1,1]
// [1, -1, -1]
// [-1, 0, 0]

// Result 1:
// [1,1,1]
// [1, 1, 1]
// [1, 0, 0]


const newMatrix = function(matrix){
    let newMatrix = [];
    let row = 0;
    let maxes = {};
    
    while (row < matrix.length){
        newMatrix.push([]);
        maxes[row] = matrix[row][0];
        
        for(let col = 0; col < matrix[row].length; col++){
                if (matrix[row][col] > maxes[row]){
                    maxes[row] = matrix[row][col];
                }
                if(matrix[row][col] === -1){
                    
                }else{
                    newMatrix[row].push
                }
        }
        row++;
    }
}