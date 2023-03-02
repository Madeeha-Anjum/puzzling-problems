<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <form method="GET" action="Solutions.php">
        <label>Insert the candies each person has separated by a comma </label>
        <input id="Candies" name="Candies"></input>
        <label>insert the extra candies</label>
        <input id="ExtraCandies" name="ExtraCandies"></input>
        <button id="Button">Submit</button>
    </form>


    <?php
    if (isset($_GET["Candies"]) && isset($_GET["ExtraCandies"])) {
        $candies = explode(',', $_GET["Candies"]);
        $extraCandies =   $_GET["ExtraCandies"];
        kidsWithCandies($candies, $extraCandies);
    }

    function kidsWithCandies($candies, $extraCandies)
    {
        $max = max($candies);
        $output = array();

        //check to see if the extra candies add to each of the kids candies is larger or equal tot he max

        for ($i = 0; $i < count($candies); $i++) {
            $currentCandies = $candies[$i] + $extraCandies;
            if ($currentCandies >= $max) {
                $output[$i] = true;
            } else {
                $output[$i] = false;
            }
        }
        print_r($output);

        /*
        Other way: 
        //add the extra candies to the first kid and compare with the rest 

        for ($i = 0; $i < count($candies); $i++) {
            $candiesTemp = $candies[$i] + $extraCandies;
            //compare to the rest 
            for ($j = 0; $j < count($candies); $j++) {
                if ($candies[$j] > $candiesTemp) {
                    $output[$i] = False;
                }
            }
            if (!isset($output[$i])) {
                $output[$i] = True;
            }
        }
        */

        return $output;
    }

    // echo the solution 
    echo "";



    ?>

</body>

</html>