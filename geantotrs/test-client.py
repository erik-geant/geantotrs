import json

import click
from otrs.ticket.template import GenericTicketConnectorSOAP
from otrs.client import GenericInterfaceClient
from otrs.ticket.objects import Ticket, Article, DynamicField, Attachment


def validate_params(ctx, param, value):
    return json.loads(value.read())


@click.command()
@click.option(
    "--params",
    required=True,
    type=click.File(),
    callback=validate_params,
    default=open("otrs.json"))
def cli(params):
 
    client = GenericInterfaceClient(
        params["server_uri"],
        tc=GenericTicketConnectorSOAP(params["webservice_name"]))
    
    # user session
    client.tc.SessionCreate(
        user_login=params["username"],
        password=params["password"])
    
    # returns all the tickets of customer 42
    #tickets = client.tc.TicketSearch(CustomerID=42)
    for ticketid in client.tc.TicketSearch():
    # for ticketid in (230188, 2301887):
        ticket = client.tc.TicketGet(
            ticketid,
            get_articles=True,
            get_dynamic_fields=False,
            get_attachments=False)
        articles = ticket.articles()
    #        article.save_attachments(r'C:\temp')
        print("TicketID: %r" % ticket.TicketID)
        print("Title: %r" % ticket.Title)
        print("CustomerID: %r" % ticket.CustomerID)
        # print("CustomerUserID: %r" % ticket.CustomerUserID)
        print("Owner: %r" % ticket.Owner)
        print("Priority: %r" % ticket.Priority)
        print("Queue: %r" % ticket.Queue)
        print("State: %r" % ticket.State)
        print("StateType: %r" % ticket.StateType)
        print("Type: %r" % ticket.Type)
        print("")
        # print(ticket)
    
    # for t in client.tc.TicketSearch():
    #     print(t)


if __name__ == "__main__":
    cli()
