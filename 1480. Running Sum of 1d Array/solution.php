<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <?php

    $nums = [1, 2, 3, 4];
    runningSum($nums); //calling the function

    function runningSum($nums)
    {
        $output = array();

        for ($i = 0; $i < count($nums); $i++) {
            if ($i == 0) {
                $output[$i] = $nums[$i];
            } else {

                $output[$i] = $nums[$i] + $output[$i - 1];
            }
        }

        return $output;
    }




    ?>

</body>

</html>