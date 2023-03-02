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
        <label>enter first persons money separated with a comma
            and the second person money separated by collin</label>
        <div>
            <input name="account" type="text">
        </div>
        <div>
            <button type="submit">Submit </button>
        </div>
    </form>
    <?php
    $accounts  = array();

    if (isset($_GET["account"])) {
        $EachPerson = explode(';', $_GET["account"]); //array og pe
        for ($i = 0; $i < count($EachPerson); $i++) {
            $accounts[$i] = explode(',', $EachPerson[$i]); //array og pe
        }
        maximumWealth($accounts);
    }

    function maximumWealth($accounts)
    {
        $totalMoney = array();
        // Add the accounts[i] values and compare to each-other
        for ($i = 0; $i < count($accounts); $i++) {
            $person = $accounts[$i];
            $totalMoney[$i] = array_sum($person);
        }
        //get the max value in array total money

        return (max($totalMoney));
    }





    ?>




</body>

</html>