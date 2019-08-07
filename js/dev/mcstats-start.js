var loader = new Loader(function() {
    mcstats.init();
    window.onhashchange(); // navigate
});

loader.addRequest('data/summary.json.gz', function(summary) {
    // load db
    mcstats.info = summary.info;
    mcstats.players = summary.players;
    mcstats.awards = summary.awards;
    mcstats.hof = summary.hof;

    // fill server info
    serverName = JSON.parse('"' + mcstats.info.serverName + '"');
    serverNameNoFmt = mcstats.removeColorCodes(serverName);

    document.title.innerHTML = `${serverNameNoFmt} &ndash; Stats`;
    document.getElementById('server-name').innerHTML = mcstats.formatColorCode(serverName);
    document.getElementById('update-time').textContent = formatTime(mcstats.info.updateTime);

    var serverIcon = document.getElementById('server-icon');
    if(!mcstats.info.hasIcon) {
        serverIcon.style.display = 'none';
    } else {
        serverIcon.setAttribute('title', serverNameNoFmt);
    }

    // sort award keys by award title
    for(var key in mcstats.awards) {
        mcstats.awardKeysByTitle.push(key);
    }

    // Set the player name for autocomplete
    var pseudos  = [];
    for(var key in mcstats.players){
        var name = mcstats.players[key].name;
        pseudos.push({name, key});
    }
    pseudos.sort((a,b) => a.name.localeCompare(b.name));
    pseudos.forEach((x,i) => {
        mcstats.autocomplete.append(mcstats.selectWidget(x.key, x.name))
    })
    mcstats.autocomplete.hide();
    $("#autocomplete li a").hover(function(){
        $(".selected").removeClass("selected");
        $(this).addClass("selected");
    });


    mcstats.awardKeysByTitle.sort(function(a,b) {
        return mcstats.awards[a].title.localeCompare(
            mcstats.awards[b].title);
    });
}, true); // compressed!

// Start
mcstats.showLoader();

loader.start();
