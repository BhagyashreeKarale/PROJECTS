import React, {useState, useEffect} from 'react'
import {commerce} from './lib/commerce';
import {Products,Navbar,Cart, Checkout} from './components';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

const App = () => {
    const [products,setProducts] = useState([]);
    const [cart,setCart] = useState({});
    const [order, setOrder] = useState({});
    const [errorMessage, setErrorMessage] = useState('');

    const fetchProducts = async () => {
        const {data} = await commerce.products.list();
        setProducts(data);
    }

    const fetchCart = async () => {
        const res = await commerce.cart.retrieve();
        setCart(res);
    }

    const refreshCart = async () => {
        const newCart = await commerce.cart.refresh();
    
        setCart(newCart);
    };

    const handleCaptureCheckout = async (checkoutTokenId, newOrder) => {
        try {
          const incomingOrder = await commerce.checkout.capture(checkoutTokenId, newOrder);
    
          setOrder(incomingOrder);
    
          refreshCart();
        } catch (error) {
          setErrorMessage(error.data.error.message);
        }
      };

    const handleAddToCart = async (productId,quantity) => {
        const res = await commerce.cart.add(productId,quantity);
        setCart(res.cart);
    }

    const handleUpdateCartQty = async (productId,quantity) => {
        const res = await commerce.cart.update(productId,{quantity});
        setCart(res.cart)
    }

    const handleRemoveFromCart = async (productId) => {
        const res = await commerce.cart.remove(productId);
        setCart(res.cart)
    }

    const handleEmptyCart = async () => {
        const res = await commerce.cart.empty();
        setCart(res.cart)
    }

    useEffect(() =>{
        fetchProducts();
        fetchCart();
    },[])

    console.log(cart);

    return (
        <Router>
            <div>
                <Navbar totalItems={cart.total_items} />
                <Switch>
                    <Route exact path="/">
                        <Products products={products} onAddToCart={handleAddToCart}/>
                    </Route>
                    <Route path="/cart">
                        <Cart 
                            cart={cart} 
                            handleEmptyCart={handleEmptyCart}
                            handleRemoveFromCart={handleRemoveFromCart}
                            handleUpdateCartQty={handleUpdateCartQty}
                        />
                    </Route>
                    <Route path="/checkout">
                        <Checkout 
                            cart={cart} 
                            order={order}
                            onCaptureCheckout={handleCaptureCheckout}
                            error={errorMessage}    
                        />
                    </Route>
                </Switch>
            </div>
        </Router>
    )
}

export default App
