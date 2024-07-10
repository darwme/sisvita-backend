const eurekaHost= process.env.EUREKA_CLIENT_SERVICEURL_DEFAULTZONE || "127.0.0.1"

const routesToSearch = 4;
export async function findRoutes() {
    let routes = await fetchRoutes();
    while (!routes) {
        routes = await fetchRoutes();
    }
    return routes;
}

async function fetchRoutes() {
    try {
        const response = await fetch('http://' + eurekaHost + ':8761/eureka/v2/apps');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.text();
        let applications = data.split("<application>")
        let result= applications.map(app => {
            let name = app.split(new RegExp("<name>(.*?)</name>"))[1];
            let hostName = app.split(new RegExp("<hostName>(.*?)</hostName>"))[1];
            let port = app.split(new RegExp("<port enabled=\"true\">(.*?)</port>"))[1];
            return { name: name, url: "http://" + hostName + ":" + port };
        });
        if(result.length !== routesToSearch )
        {
            console.log(result);
            console.log(result.length === routesToSearch)
            throw new Error("Routes not founded");
        }
        return result;
    } catch (error) {
        console.error('Error fetching routes:', error);
        await new Promise(resolve => setTimeout(resolve, 5000));
        return null;
    }
}

