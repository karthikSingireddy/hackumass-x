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
                this.drawTable(30, 30, 20, 20, !false);
                break;
            case 'frank':
                frank.draw(ctx, this.canvas.current);
                break;
            case 'hamp':
                hamp.draw(ctx, this.canvas.current);
                break;
            case 'berk':
                berk.draw(ctx, this.canvas.current);
                break;
            default:
                break
        }
    }

    drawTable(x, y, width, height, taken) {
        const canvas = this.canvas.current;
        const ctx = canvas.getContext('2d');
        const color = taken ? '#FF0000' : '#00FF00';

        ctx.fillStyle = color;
        ctx.fillRect(x, y, width, height);
    }

    render() {
        console.log(this.props.name);
        return <div className='mapContainer'>
            <canvas ref={this.canvas}/>
        </div>
    }
}

export default DiningHall;