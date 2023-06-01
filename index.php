<?php
try {
    $bdd = new PDO("mysql:host=localhost;dbname=score;charset=utf8", 'root' , 'EcoleIT123!');
}catch (Exception $e){
    echo "Erreur :" . $e->getMessage();
}
$id = $bdd->prepare('SELECT * FROM score ORDER BY score DESC');
$id->execute();
?>

<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="st.css" rel="stylesheet" type="text/css">
    <link rel="icon" type="image/x-icon" href="mkdir/casse-brique128.png">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Break-IT</title>
</head>
<body>
    <div id="background"></div>
    <nav>
        <a href="#home">HOME</a>
        <a href="#jeux">GAME</a>
        <a href="#info">INFO</a>
        <a href="#download">DOWNLOAD</a>
        <a href="#contact">CONTACT</a>
    </nav>
    <button class="burger" type="button" aria-label="toggle curtain navigation" id="home">
        <span id="span1"></span>
        <span id="span2"></span>
        <span id="span3"></span>
    </button>
    <div class="container">
        <div class="centered">
            <h1 id="title">Break-IT</h1>
        </div>
    </div>
    <div class="degrade"></div>
    <span id="span4"></span>
    <div id="block">
        <div id="jeux">
            <h2>GAME</h2>
                <div class="img_txt">
                    <img alt="img_jeux" src="mkdir/330px-Screenshot-LBreakout2.jpg" id="img_break_it">
                    <div class="txt_block">
                        <h4>Qu'est-ce que le Casse brique ?</h4>
                        <p>Le casse-briques est un genre de jeu vidéo souvent classé dans la catégorie arcade,
                            apparu en 1976 avec le jeu Breakout. Il est directement inspiré de Pong.
                            Le principe général est de détruire, au moyen d'une ou plusieurs balles,
                            un ensemble de briques se trouvant dans un niveau pour accéder au niveau suivant.</p>
                    </div>
                </div>
        </div>
        <div id="info">
            <h2>INFO</h2>
            <div class="txt_block">
                <h4>Les règles et comment y jouer ?</h4>
                <p>Le joueur contrôle une planche qu'il peut déplacer de gauche à droite sur un axe horizontal au bas de l'écran,
                    et le but est d'empêcher la balle de franchir cette ligne en l'interceptant avec la raquette.
                    S'il y parvient, la balle est renvoyée en direction des briques et les casse si il la touche ; dans le cas contraire,
                    le joueur perd la balle. Si cette balle est la dernière qui lui reste, il perd la partie.

                    Toute la difficulté consiste donc à rattraper la balle lorsqu'elle se déplace vite
                    et de casser toutes les briques présentent sur la planche du jeu pour gagner.</p>
            </div>
        </div>
        <div id="download">
            <h2>DOWNLOAD</h2>
            <a href="tech/modeDemploie" download="Fiche technique"><button type="button" id="btn_download">Download</button></a>
        </div>
        <div id="score_board">
            <h2>TOP SCORE</h2>
                <?php
                echo '<div id="table_score">';
                $place = 0;
                echo '<div class="alignement_score">';
                echo '<p>PLACE</p>';
                echo '<p>PSEUDO</p>';
                echo '<p>SCORE</p>';
                echo '<p>DATE</p>';
                echo '</div>';
                while ($ligne = $id->fetch(PDO::FETCH_ASSOC)) {
                    $identifiant = htmlspecialchars($ligne['id']);
                    $place++;
                    echo '<div class="alignement_score">';
                    echo '<p>' .htmlspecialchars($place). '.</p>';
                    echo '<p>' .htmlspecialchars($ligne['name']). '</p>';
                    echo '<p>' .htmlspecialchars($ligne['score']). '</p>';
                    echo '<p>' .htmlspecialchars($ligne['date']). '</p>';
                    echo '<span id="span5"></span>';
                    echo '</div>';
                }
                echo '</div>';
                ?>
        </div>
        <div id="contact">
            <h2>CONTACT</h2>
            <div class="img_txt">
                <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16" color="white" >
                    <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
                </svg>
                <p>+33 7 56 49 26 23</p>
            </div>
            <div class="img_txt" id="endessous">
                <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-mailbox" viewBox="0 0 16 16" color="white">
                    <path d="M4 4a3 3 0 0 0-3 3v6h6V7a3 3 0 0 0-3-3zm0-1h8a4 4 0 0 1 4 4v6a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V7a4 4 0 0 1 4-4zm2.646 1A3.99 3.99 0 0 1 8 7v6h7V7a3 3 0 0 0-3-3H6.646z"/>
                    <path d="M11.793 8.5H9v-1h5a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.354-.146l-.853-.854zM5 7c0 .552-.448 0-1 0s-1 .552-1 0a1 1 0 0 1 2 0z"/>
                </svg>
                <p>break-it@ecole-it.com</p>
            </div>
        </div>
    </div>

    <script>
        const burger = document.querySelector('.burger');
        const navi = document.querySelector('nav')

        burger.addEventListener("click", toggleNav)

        function toggleNav(){
            burger.classList.toggle("active");
            navi.classList.toggle("descent");
        }
    </script>
</body>
