using Microsoft.Crm.Sdk.Messages;
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Tooling.Connector;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.Net;
using ApiWorkshop.Models.Dynamics;
using Microsoft.Xrm.Sdk.Query;

namespace DynamicsWorkshop
{
    public class DynamicsUtil
    {
        private static IOrganizationService _service = null;
        public static void Main(string[] args)
        {
            // Get a handle on the OrgService
            var service = GetOrgService();
            // Retrieve an account record with some fields.
            var accountId = Guid.Parse("73852CEB-84A2-4099-9B34-1DCCE3D22902");
            service.Retrieve("account", accountId, new ColumnSet(new string[] {"name", "accountnumber"});
        }
        public static IOrganizationService GetOrgService()
        {
            if (_service == null)
            {   
                // A sample connection string looks like this (in the application config file)
                // <add name="MyCrmEnvConnStr" connectionString="AuthType=IFD; Url=UrlToDynamicsInstance; DOMAIN=myDomain; Username=myUserName@myDomain.com; Password=myPassword" />
                // NOTE: AuthType can be any of the following:
                // IFD = Internet-facing deployment
                // For more details - see https://docs.microsoft.com/en-us/powerapps/developer/data-platform/xrm-tooling/use-connection-strings-xrm-tooling-connect
                
                CrmServiceClient crmSvc = new CrmServiceClient(ConfigurationManager.ConnectionStrings["MyCrmEnvConnStr"].ConnectionString);

                _service = (IOrganizationService)crmSvc.OrganizationWebProxyClient != null ? (IOrganizationService)crmSvc.OrganizationWebProxyClient : (IOrganizationService)crmSvc.OrganizationServiceProxy;

                // Execute a simple "WhoAmI" request to test the connection.
                var whoAmIReq = new WhoAmIRequest();
                var resp = (WhoAmIResponse)_service.Execute(whoAmIReq);
                Console.WriteLine($"Welcome {resp.UserId}");

                return _service;
            }
            else
                return _service;

        }
    }
}
