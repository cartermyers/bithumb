"use strict";

(function () {

	function OnRegisterSWError(e)
	{
		console.warn("Failed to register service worker: ", e);
	};

	// Runtime calls this global method when ready to start caching (i.e. after startup).
	// This registers the service worker which caches resources for offline support.
	window.C3_RegisterSW = function C3_RegisterSW()
	{
		if (!navigator.serviceWorker)
			return;		// no SW support, ignore call

		try {
			navigator.serviceWorker.register("../static/game/sw.js", { scope: "../static/game/" })
			.then(function (reg)
			{
				console.log("Registered service worker on " + reg.scope);
			})
			.catch(OnRegisterSWError);
		}
		catch (e)
		{
			OnRegisterSWError(e);
		}
	};

})();
