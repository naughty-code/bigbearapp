$(document).ready(function() {
	function search() {
		var alertErrorCabins = $('#alert-danger-cabins')
		var progressBarCabins = $('#progress-cabins')
		progressBarCabins.removeClass('d-none')
		alertErrorCabins.addClass('d-none')

		$.get('/api/cabins')
			.done(function( data ) {
				progressBarCabins.addClass('d-none')
				$('#cabins').DataTable( {
					data: data,
					columns: [
						{ title: "IDVRM" },
						{ title: "ID" },
						{ title: "NAME" },
						{ title: "WEBSITE" },
						{
							title: "DESCRIPTION",
							render: function ( data, type, row ) {
								return `<span class="d-inline-block text-truncate" data-toggle="tooltip" style="max-width: 150px;" title="${data}">
								${data}
							  </span>`;
							}
						},
						{ title: "ADRESS" },
						{ title: "LOCATION" },
						{ title: "BEDROOMS" },
						{ title: "OCCUPANCY" },
						{ title: "TIER" },
						{ title: "STATUS" }
					]
				} );
				$('[data-toggle="tooltip"]').tooltip();
			})
			.fail(function() {
				progressBarCabins.addClass('d-none')
				alertErrorCabins.removeClass('d-none')
			})
	}
	search();
});