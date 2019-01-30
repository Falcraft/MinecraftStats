// Initialize
var mcstats = {
    loader: $('#loader'),

    infoBox: $('#info'),
    content: $('#content'),
    footer: $('#footer'),

    view: $('#view'),
    viewTitle: $('#view-title'),
    viewSubtitle: $('#view-subtitle'),
    viewDesc: $('#view-desc'),
    viewIcon: $('#view-icon'),
    viewContent: $('#view-content'),
    playerSearch : $("#player-search"),
    autocomplete : $("#autocomplete"),

    info: {},
    awards: {},
    awardKeysByTitle: [],
    players: {},
    playerIdsByName: [],
    maxAutoComplete : 10,
};

// Initialize client
mcstats.init = function() {
    mcstats.infoBox.css('display', 'block');
    mcstats.content.css('display', 'block');
}

// Show loader and nothing else
mcstats.showLoader = function() {
    mcstats.content.hide();
    mcstats.loader.show();
}

// Show view - content shall be prepared before calling this
mcstats.showView = function(title, subtitle, desc, iconUrl) {
    mcstats.viewTitle.html(title);

    if(subtitle) {
        mcstats.viewSubtitle.html(subtitle);
        mcstats.viewSubtitle.show();
    } else {
        mcstats.viewSubtitle.hide();
    }

    if(desc) {
        mcstats.viewDesc.html(desc);
        mcstats.viewDesc.show();
    } else {
        mcstats.viewDesc.hide();
    }

    if(iconUrl) {
        mcstats.viewIcon.attr('src', iconUrl);
        mcstats.viewIcon.show();
    } else {
        mcstats.viewIcon.hide();
    }

    mcstats.loader.hide();
    mcstats.content.show();
}

// Collapse navbar when an item is clicked
$('.nav-link').on('click', function() {
    $('.collapse').collapse('hide');
});


$('#player-form').on('submit', function() {
    var selected = $("#autocomplete li a.selected");
    if(selected.length){
        mcstats.playerSearch.val("");
        location.hash = selected[0].getAttribute("href");
        return;
    } 
    var id = mcstats.playerSearch.val();
    mcstats.playerSearch.val("");
    for(var k in mcstats.players) {
        var name = mcstats.players[k].name;
        if(name.toLowerCase() === id.toLowerCase()){
            return location.hash = "player:" + k;
        }
    }
    location.hash = "player:null";
    return false;
});

mcstats.playerSearch.keydown(function(ev){
    if(ev.which === 40){ // up
        var next = $(".selected").parent().nextAll(':visible:first');
        if(next.length){
            $(".selected").removeClass("selected");
            next.children("a").addClass("selected");
            return false;
        }
    } else if(ev.which === 38){ //down
        var prev = $(".selected").parent().prevAll(':visible:first');
        if(prev.length){
            $(".selected").removeClass("selected");
            prev.children("a").addClass("selected");
            return false;
        }
    }

    return true;
});

window.addEventListener('click', function(){
    mcstats.autocomplete.hide();
});

$("#player-search").on('input', function () {
    var entered = mcstats.playerSearch.val().toLowerCase();
    if(!entered){
        mcstats.autocomplete.hide()
    } else {
        var total = mcstats.maxAutoComplete;
        $(".selected").each(function(id,el){
            $(el).removeClass("selected");
        });
        mcstats.autocomplete.children('li').each(function(c, el) {
            var $el = $(el);
            var txt = $el.text().trim().toLowerCase();
            if(total <= 0){
                $el.hide();
                return;
            }
            if(txt.indexOf(entered) > -1){
                $el.show();
                if(total === mcstats.maxAutoComplete){
                    $el.children("a").addClass("selected");
                }
                total--;
            } else {
                $el.hide();
            }
        });

        mcstats.autocomplete.show();
    }
});


// Register navigation event handler
window.onhashchange = function() {
    window.scrollTo(0, 0);
    mcstats.showLoader();

    var hash = window.location.hash;
    if(hash.startsWith('#award:')) {
        // open award view
        var id = hash.substr(7);
        mcstats.showAward(id);
    } else if(hash.startsWith('#player:')) {
        // open player view
        var uuid = hash.substr(8);
        mcstats.showPlayer(uuid);
    } else if(hash == '#players') {
        // go to player list
        mcstats.showPlayerList();
    } else if(hash == '#hof') {
        // go to hall of fame
        mcstats.showHof();
    } else if(hash == '#loader') {
        // stick with loader - for debugging purposes
    } else {
        // go to awards list (default)
        mcstats.showAwardsList();
    }
};


