mcstats.showHof = function() {
    var tbody = '';

    var rank = 1;
    mcstats.hof.forEach(function(entry) {
        var rankWidget = mcstats.rankWidget(rank++, 'crown');
        var playerWidget = mcstats.playerWidget(entry.uuid);
        var value = entry.value;

        tbody += `
            <tr>
                <td class="text-right">${rankWidget}</th>
                <td>${playerWidget}</td>
                <td class="text-data text-center">${value[1]}</td>
                <td class="text-data text-center">${value[2]}</td>
                <td class="text-data text-center">${value[3]}</td>
                <td class="text-data text-right">${value[0]}</td>
            </tr>
        `;
    });

    mcstats.viewContent.html(`
        <div class="mcstats-entry p-1">
        <div class="round-box p-1">
            <table class="table table-responsive-xs table-hover table-sm">
            <thead>
                <th scope="col" class="text-right text-shadow">Classement</th>
                <th scope="col" class="text-shadow">Joueur</th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Médailles d'or" src="img/fatcow/medal_award_gold.png"/></th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Médailles d'argent" src="img/fatcow/medal_award_silver.png"/></th>
                <th scope="col" class="text-center"><img class="img-textsize-2" title="Médailles de bronze" src="img/fatcow/medal_award_bronze.png"/></th>
                <th scope="col" class="text-right text-shadow">Score</th>
            </thead>
            <tbody>${tbody}</tbody>
            </table>
        </div>
        </div>
    `);

    // show
    mcstats.showView(
        'Panthéon',
        'Classement par score',
        `
Le score est calculé en utilisant les médailles détenues par le joueur.<br/>
Une médaillte d'or vaut 4 points, une médaille d'argent 2 points et une médaille de bronze 1 point.
        `,
        false);
}
