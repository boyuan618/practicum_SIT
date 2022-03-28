from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )

        # Add links
        self.addLink(H1, S2)
        self.addLink(H2, S3)
        self.addLink(S2, S3)
        self.addLink(S2, S1)
        self.addLink(S1, S3)
        


topos = { 'mytopo': ( lambda: MyTopo() ) }