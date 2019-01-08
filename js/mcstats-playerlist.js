mcstats.showPlayerList = function() {
    var tbody = '';
    mcstats.playerIdsByName.forEach(function(uuid) {
        var player = mcstats.players[uuid];

        var rowClass = mcstats.isActive(player.last) ? '' : 'inactive';
        var widget = mcstats.playerWidget(uuid);
        var last = mcstats.lastOnlineWidget(player.last);

        tbody += `
            <tr class="${rowClass}">
                <td>${widget}</td>
                <td class="text-right">${last}</td>
            </tr>
        `;
    });

    mcstats.viewContent.html(`
        <div class="text-center mt-3">
            <input id="show-inactive" type="checkbox"/>
            <label for="show-inactive">Afficher les joueurs inactifs</label>
        </div>
        <div class="mcstats-entry p-1">
        <div class="round-box p-1">
            <table class="table table-responsive-xs table-hover table-sm">
            <thead>
                <th scope="col" class="text-shadow">Joueur</th>
                <th scope="col" class="text-right text-shadow">Dernière connexion</th>
            </thead>
            <tbody>${tbody}</tbody>
            </table>
        </div>
        </div>
    `);

    // hide inactive by default
    $('.inactive').hide();

    // click event for checkbox
    $('#show-inactive').click(function() {
        $('.inactive').toggle(this.checked);
    });

    // show
    mcstats.showView(
        'Liste des joueurs',
        false,
        `
            Les joueurs qui ne se sont pas connectés depuis ${mcstats.info.inactiveDays} jours
            sont consiérés comme inactifs et ne sont pas éligibles pour les prix
        `,
        false);
}
