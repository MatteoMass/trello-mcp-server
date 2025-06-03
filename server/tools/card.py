"""
This module contains tools for managing Trello cards.
"""

import logging
from typing import List

from mcp.server.fastmcp import Context

from server.models import TrelloCard
from server.services.card import CardService
from server.trello import client
from server.dtos.update_card import UpdateCardPayload

logger = logging.getLogger(__name__)

service = CardService(client)


async def get_card(ctx: Context, card_id: str) -> TrelloCard:
    """Retrieves a specific card by its ID.

    Args:
        card_id (str): The ID of the card to retrieve.

    Returns:
        TrelloCard: The card object containing card details.
    """
    try:
        logger.info(f"Getting card with ID: {card_id}")
        result = await service.get_card(card_id)
        logger.info(f"Successfully retrieved card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def get_cards(ctx: Context, list_id: str) -> List[TrelloCard]:
    """Retrieves all cards in a given list.

    Args:
        list_id (str): The ID of the list whose cards to retrieve.

    Returns:
        List[TrelloCard]: A list of card objects.
    """
    try:
        logger.info(f"Getting cards for list: {list_id}")
        result = await service.get_cards(list_id)
        logger.info(f"Successfully retrieved {len(result)} cards for list: {list_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to get cards: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def create_card(
    ctx: Context, list_id: str, name: str, desc: str | None = None
) -> TrelloCard:
    """Creates a new card in a given list.

    Args:
        list_id (str): The ID of the list to create the card in.
        name (str): The name of the new card.
        desc (str, optional): The description of the new card. Defaults to None.

    Returns:
        TrelloCard: The newly created card object.
    """
    try:
        logger.info(f"Creating card in list {list_id} with name: {name}")
        result = await service.create_card(list_id, name, desc)
        logger.info(f"Successfully created card in list: {list_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to create card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def update_card(
    ctx: Context, card_id: str, payload: UpdateCardPayload
) -> TrelloCard:
    """Updates a card's attributes.

    Args:
        card_id (str): The ID of the card to update.
        **kwargs: Keyword arguments representing the attributes to update on the card.

    Returns:
        TrelloCard: The updated card object.
    """
    try:
        logger.info(f"Updating card: {card_id} with payload: {payload}")
        result = await service.update_card(
            card_id, **payload.model_dump(exclude_unset=True)
        )
        logger.info(f"Successfully updated card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to update card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise


async def delete_card(ctx: Context, card_id: str) -> dict:
    """Deletes a card.

    Args:
        card_id (str): The ID of the card to delete.

    Returns:
        dict: The response from the delete operation.
    """
    try:
        logger.info(f"Deleting card: {card_id}")
        result = await service.delete_card(card_id)
        logger.info(f"Successfully deleted card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to delete card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise

async def assign_card_to_member(ctx: Context, card_id: str, member_id: str) -> TrelloCard:
    """Retrieves a specific card by its ID.

    Args:
        card_id (str): The ID of the card to retrieve.
        member_id (str): The ID of the member to assign to the card.

    Returns:
        TrelloCard: The card object containing card details.
    """
    try:
        logger.info(f"Getting card with ID: {card_id}")
        result = await service.assign_card_to_member(card_id, member_id)
        logger.info(f"Successfully assigned card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to assign card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
    
async def move_card_to_list(ctx: Context, card_id: str, list_id: str) -> TrelloCard:
    """Moves a card to a different list.
    Args:
        card_id (str): The ID of the card to move.
        list_id (str): The ID of the list to move the card to.
    Returns:
        TrelloCard: The moved card object.
    """     

    try:
        logger.info(f"Moving card with ID: {card_id}")
        result = await service.move_card_to_list(card_id, list_id)
        logger.info(f"Successfully moved card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to move card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise

async def add_comment_to_card(ctx:Context, card_id:str, comment: str) -> TrelloCard:
    """Adds a comment to a card.

    Args:
        card_id (str): The ID of the card to add the comment to.
        comment (str): The content of the comment.

    Returns:
       TrelloCard: The response from the comment addition operation.
    """
    try:
        logger.info(f"Adding commento to card with ID: {card_id}")
        result = await service.add_comment_to_card(card_id, comment)
        logger.info(f"Successfully added comment to card: {card_id}")
        return result
    except Exception as e:
        error_msg = f"Failed to add comment to card: {str(e)}"
        logger.error(error_msg)
        await ctx.error(error_msg)
        raise
