import { 
    CART_ADD_ITEM, 
    CART_REMOVE_ITEM 
} from "../constants/cartConstants";



export const cartReducer = (state={cartItems:[]}, action) => {
    switch(action.type){
        case CART_ADD_ITEM:
            const item = action.payload
            // checks if item exists
            const existItem = state.cartItems.find(x => x.product === item.product)

            // if item matches one in the cart, replace it with item added/quantity, 
            // else return original state with item added to cart
            if(existItem){
                return {
                    ...state,
                    cartItems: state.cartItems.map(x=> 
                        x.product === existItem.product ? item : x
                        )
                }
            }else{
                return{
                    ...state,
                    cartItems:[...state.cartItems, item]
                }
            }

        case CART_REMOVE_ITEM:
            return{
                ...state,
                cartItems:state.cartItems.filter(x => x.product !== action.payload)
            }
            
        default:
            return state
    }
}