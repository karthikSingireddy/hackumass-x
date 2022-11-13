import React from 'react'
import berk from './berk';
import './diningHall.css'
import frank from './frank';
import hamp from './hamp';
import woo from './woo';

class DiningHall extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
        this.props = props;
        this.canvas = React.createRef();
    }

    componentDidMount() {
        this.componentDidUpdate(null, null);
    }

    componentDidUpdate(p, c) {
        const ctx = this.canvas.current.getContext('2d');
        ctx.clearRect(0, 0, this.canvas.current.width, this.canvas.current.height);
        switch(this.props.name) {
            case 'worcester':
                woo.draw(ctx, this.canvas);
                break;
            case 'frank':
                frank.draw(ctx, this.canvas);
                break;
            case 'hamp':
                hamp.draw(ctx, this.canvas);
                break;
            case 'berk':
                berk.draw(ctx, this.canvas);
                break;
            default:
                break
        }
    }

    render() {
        console.log('rendered')
        return <div className='mapContainer'>
            <canvas ref={this.canvas}/>
        </div>
    }
}

export default DiningHall;