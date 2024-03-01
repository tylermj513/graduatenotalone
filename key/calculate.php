<?php
$p = json_decode($_POST['p']);
$q = json_decode($_POST['q']);

$size = count($q);

function printMatrix($matrix) {
    echo "<pre>";
    foreach ($matrix as $row) {
        foreach ($row as $cell) {
            echo $cell . " ";
        }
        echo "<br>";
    }
    echo "</pre>";
}

function optimalBST($p, $q) {
    global $size;
    $e = array_fill(0, $size + 1, array_fill(0, $size, INF));
    $root = array_fill(0, $size, array_fill(0, $size, 0));

    // Optimal BST calculation logic here...
    // This part should be implemented based on your C++ logic.

    // For demonstration, let's just return the matrices
    echo "<h2>Cost Matrix:</h2>";
    printMatrix($e);
    echo "<h2>Root Matrix:</h2>";
    printMatrix($root);
}

optimalBST($p, $q);
?>
